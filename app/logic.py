from app.geocoding import get_coordinates
from app.property_loader import load_properties
from app.distance_calc import haversine
from app.models import PropertyListResponse, Property
from app.llm_location import extract_locations_from_query

async def find_nearby_properties(location_query: str) -> PropertyListResponse:
    #print(" Location query:", location_query)
    place_names = extract_locations_from_query(location_query)
    print(" LLM extracted:", place_names)

    if not place_names:
        

        return PropertyListResponse(properties=[], message="No location found in the query.")

    properties = load_properties()
    all_nearby = []

    for place in place_names:
        coords = get_coordinates(place)
        print(f"Geocoded: {place} → {coords}")
        if not coords:
            continue

        lat1, lon1 = coords

        for prop in properties:
            dist = haversine(lat1, lon1, prop["latitude"], prop["longitude"])
            print(f" {place} , {prop['property']} = {dist:.2f} km")
            if dist <= 50:
                all_nearby.append(Property(
                    name=prop["property"],
                    latitude=prop["latitude"],
                    longitude=prop["longitude"],
                    distance_km=round(dist, 2)
                ))

    if all_nearby:
        all_nearby.sort(key=lambda x: x.distance_km)
        return PropertyListResponse(properties=all_nearby)
    else:
        return PropertyListResponse(properties=[], message="No properties found within 50 km.")