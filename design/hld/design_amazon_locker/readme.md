Given
Users should be able to use a code to open a locker and pick up a package
Delivery guy should be able to find an "optimal" locker for a package
Then
Free coding from scratch in any language
What I did
I used Vec<Locker> to represent the state.

The interviewer asked if I can improve the code.

I told I could probably use a HashMap (Size -> Locker) if there are standard sizes like (small, medium, large instead of (w,h,d))

Got rejected

trait Volumable {
    fn get_volume(&self) -> u32;
}

#[derive(Debug, PartialEq)]
pub struct Package {
    w: u32,
    h: u32,
    d: u32,
}

impl Volumable for Package {
    fn get_volume(&self) -> u32 {
        self.w * self.h * self.d
    }
}

#[derive(Debug, PartialEq)]
pub struct Locker {
    w: u32,
    h: u32,
    d: u32,

    code: u32,
    occupied: bool,
}

impl Volumable for Locker {
    fn get_volume(&self) -> u32 {
        self.w * self.h * self.d
    }
}

pub fn get_optimal_locker<'a>(
    lockers: &'a Vec<Locker>,
    package: &Package,
) -> Option<&'a Locker> {
    lockers
        .iter()
        .filter(|l| !l.occupied)
		
		// simplifying here but I wrote a custom fit function to check (w, h, d)
        .filter(|l| package.get_volume() <= l.get_volume())
		
        .min_by_key(|l| l.get_volume())
}

pub fn get_locker_by_code<'a>(lockers: &'a Vec<Locker>, code: u32) -> Option<&'a Locker> {
    lockers.iter().find(|l| l.code == code)
}










Amazon Locker

Requirements :-

Assign a closest locker to a person given current co-ordinates( where customer wants )
After order is delivered by courier service to customer specified amazon locker, a 6 digit code will be sent to customer .
Item will be placed in Amazon locker for 3 days
After 3 days, if Item is not picked up from the locker, refund process will be initiated
Amazon locker will be assigned to customer based on the size of the locker ( S,M,L,XL,XXL)
Only items that are eligible to be put in locker can be assigned to amazon locker .i.e Not all items can be placed inside locker (like furniture can't be put inside amazon locker)
Access to Amazon locker will depend on Store's opening and closing time.(Since Amazon locker are placed inside stores,malls etc)
Items can be returned to Amazon locker as well .
Items that are eligible Amazon locker item, can only be returned by customer
Once the Door is closed. User's code will be expired. (User will not be able to open the locker now)
Questions I will ask from interviewer :

Who are my customers ? probable answer would be courier guys (For delivery : FedX,Bluedart and For accepting order : Customer who buys)
How many are they?
Is this service to avail globally or to certain cities within a country ?
How many user request may come in a single minute ?
Scenario :

Customer added (amazon locker eligible) item in a cart from amazon.com
there will be cart Microservice that will forward the request to Amazon locker location tracking service based on current location of the user, item size requested
Internal server api call will contains following parameters
List find_Locker(item_id,size_requested,customer_latitude,customer_longitude)

This will find all the lockers based on the size_requested by the customer
All the lockers can be put in a data structure like (K_dimension tree), to effectively search lockers, based on k dimensions
where dimesnsions could be location,size,availibility

Each locker Obect have the property
Locker {
Locker_id
size,
locker_status
}

locker_status {
Booked
Free

}

on next screen user will get the list of nearest amazon lockers available with their address details and their closing and opening timings.

User selects one of the amazon locker from the given lockers location list

api request like (item_id, locker_id,payment_status,expected_delivery_date) will be made from the client side.
6a. Now the locker_id status will be changed to BOOKED, only when payment Status = OK
6a i. when the locker is booked, an RDMS transaction will be commited and locker_status will be changed to BOOKED
Note : we will use RDMS database (MySQL) because locker booking status needs consistency. so MYSQL transactions will provide ACID properties with BEGIN Transaction
and COMMIT feature for booking a current locker. SO that in distributed environment , other customers can not book the same locker.
6a ii. when payment_status is NOT_OK, locker_id will not be booked . error message will be spawned from the (amazon locker booking service) microservice directly to theclient

when the locker is booked. locker_staus will be : BOOKED of given locker_ID

Given locker_id will not be sent to AMAZON LOCKER.

AMAZON LOCKER -> is the actual locker at a particular store
AMAZON LOCKER will generate a two 6 digit code for a given locker_ID

one for BlueDart delivery service and will send code to
one for Customer , code will be generated after Bluedart delivery service has placed the order and closed the door.
Amazon Locker will send this code to Amazon App server.

Code generated by Amazon Locker will be sent through messaging queue.

Messaging queue(like Rabbit MQ) will send the code to app server and client(subscriber)

App server will store the code in their db as well

After customer has taken out the order from the order . Locker status will be changed to FREE and same status will be deliverd by AMAZON locker system to app server, which will in turn will update the locker_id to db.

IF AMAZON LOCKER is closed from 3 days. a request to app server is made to delivery service to pickup the item from the given locker id.

8
Show 1 reply
Reply
Share
Report
anmoluppal365's avatar
anmoluppal365
11
Last Edit: May 13, 2019 9:46 PM

Read More
Let's tackle problems one by one. The first one is a design problem and the second one being a DSA problem.

Problem 1: Users should be able to use a code to open a locker and pick up a package
The problem requires us to fabricate a solution similar to OTP system we use now-a-days for authentication. Let's assume that the delivery boy has found the most appropriate locker position. He will feed-in the unique locker ID and the consumer ID to an application which would return an OTP (4-digit or 6-digit) with a life-time of ~5 minutes. So the delivery boy action(s) would trigger an API call to generate an OTP for the unique locker ID.

The OTP would be:

Pushed to the unique locker for authentication along with TTL(Time to live: ~5minutes) and MAX_TRIES = 3.
Pushed to the client(delivery boy)
Generating the OTP:
Since the OTP is transient, so we could simply use a random number generator in this case.

Once the delivery guy closes the locker door, the current session data would be deleted and he/she has to re-authenticate, using a new OTP. Until the consumer collects the items from this locker the status of locker would be maintained as reserved.

Now assuming that the delivery boy has placed the package in the desired locker. The unique locker ID would be linked with the user ID of the person who ordered the product. In the evening when the user arrives at the locker house, the user would trigger an API which would return the unique locker ID(s) linked to his account. He can then request the OTP for the current unique locker ID. Again the same OTP generation and authentication flow would be followed. After the user closes the locker door, an API would be fired from the locker that the user has picked his/her items. The user would also be prompted on his device to confirm if he/she as actually collected his/her items. After confirmation from the user, the locker status would be changed to empty.

Problem 2: Delivery guy should be able to find an "optimal" locker for a package
The request for the optimal locker would fire an API with the locker cluster ID and dimensions of the package. The API would fetch all the lockers which are empty for the given locker cluster ID. Among all the available lockers it would find the most optimal locker ID. Finding the most optimal locker ID can be done using:

Brute force in O(N), where you try to find the locker whose length, breadth and height all are strictly greater than the length, breadth and height of the delivered item.
Using kd-Tree in O(logN).
