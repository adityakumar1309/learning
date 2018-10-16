Parking Lot

Vehicle - color, numPlate, spot_size, get_spots()

ParkingSpot - spot_capacity, is_occupied, (x,y) co-ordinates, level

ParkingManager - get_spots_needed(Vehicle vobj), ticket.issues_ticket(vehicle), generate_bill(ticket), ParkingSpot spot = getVacantSpot(Vehivle, ParkingLot), park_vehicle(vobj, spotObj), unpark_vehicle(ticket_obj)

ParkingLot - levels, gets_vacant_parking_spot(Vehicle)

Ticket - parked_time, Vehicle vobj

IParkingState - vacantState , parkedState, park(), unpark() 

Billing - Ticket obj, generate_bill()

Rate - enum VehicleType, HashMap<enum, int>

enum VehicleType - car, bus, truck, two wheeler

To make it even more flexible and powerful, the ParkingManager could use a strategy for ordering the potential free spaces to be given for a specific size of vehicle, and implementing different kind of allocation heuristics.
