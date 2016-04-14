import swapi

VEHICLE_SPEEDS = []

def get_vehicle_speeds():
    if not VEHICLE_SPEEDS:
        # Get vehicle name-speed mapping
        vehicles = swapi.get_all('vehicles')

        for vehicle in vehicles.iter():
            try:
                speed = int(vehicle.max_atmosphering_speed)
            except Exception as err:
                print err
                speed = -1
            VEHICLE_SPEEDS.append({'vehicle': vehicle.name, 'speed': speed})
    return VEHICLE_SPEEDS
