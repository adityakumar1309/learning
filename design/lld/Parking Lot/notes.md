Parking Lot

Vehicle - color, numPlate, spot_size

ParkingSpot - spot_capacity, is_occupied, (x,y) co-ordinates, level

ParkingManager - ticket.issues_ticket(vehicle), generate_bill(ticket), ParkingSpot spot = getVacantSpot(Vehivle, ParkingLot)

ParkingLot - levels, gets_vacant_parking_spot(Vehicle)

Ticket - parked_time, Vehicle vobj

IParkingState - vacantState , parkedState, park(), unpark() 

Billing - Ticket obj, generate_bill()

Rate - enum VehicleType, HashMap<enum, int>

enum VehicleType - car, bus, truck, two wheeler
