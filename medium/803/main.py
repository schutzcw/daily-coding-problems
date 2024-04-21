from typing import Dict, List, NamedTuple, Optional, Tuple

Flight = Tuple[str,str,int]


class MultiStopFlight(NamedTuple):
    flights: List[Flight]
    total_cost: int


def find_cheapest(input_list: List[Flight],
                  source: str,
                  final_destination: str,
                  n_connections: int) -> MultiStopFlight:
    """Given a list of Flight objects, a source, a destination, and a max number of connections,
    return the cheapest flight path from source to destination.

    Args:
        input_list (List[Flight]): The input list of flights.
        source (str): The source airport.
        final_destination (str): The final destination airport.
        n_connections (int): The max number of connections the person is willing to take.

    Returns:
        MultiStopFlight: The cheapest flight from source to final_destination with <=
            n_connections connecting flights. If no such flight exists, return an empty
            MultiStopFlight object.
    """

    # create a map from source city to all destination cities
    flight_map: Dict[str, List[Tuple[str,int]]] = dict()
    for flight in input_list:
        SRC = flight[0]
        dst_cost = (flight[1], flight[2])
        if SRC in flight_map:
            flight_map[SRC].append(dst_cost)
        else:
            flight_map[SRC] = [dst_cost]    

    # initialize the cheapest flight to be empty
    cheapest_path = MultiStopFlight([], 0)
    
    def cheapest(src: str, conns: int, multi_stop_flight: Optional[MultiStopFlight] = None) -> None:
        """Recursive function for finding the cheapest flight. 

        Args:
            src (str): Current starting city.
            conns (int): Max number of connections remaining.
            multi_stop_flight (Optional[MultiStopFlight], optional): The current MultiStopFlight
                object that was required to get the `src`. Defaults to None.
        """
        nonlocal cheapest_path
        
        # re-initialize if None
        if multi_stop_flight is None:
            multi_stop_flight = MultiStopFlight([], 0)

        # logging
        n_flights = len(multi_stop_flight.flights)
        PREFIX = n_flights * '\t'
        print(f"{PREFIX}cheapest(src={src}, conns={conns}, multi_stop_flight={multi_stop_flight})")

        # base case
        if conns < 0:
            return
        
        # if no flights possible
        if src not in flight_map:
            print(f"{PREFIX}{src} not in src list. Returning.")
            return
        
        # either update the cheapest flight if we've reached the final destination, or recurse.
        for (destination, cost) in flight_map[src]:
            current_cost = multi_stop_flight.total_cost + cost
            updated_flight = MultiStopFlight(multi_stop_flight.flights + [(src, destination, cost)], current_cost)
            if final_destination == destination:
                if (cheapest_path.total_cost == 0) or (current_cost < cheapest_path.total_cost):
                    cheapest_path = updated_flight
            else:
                cheapest(destination, conns - 1, updated_flight)

    cheapest(source, n_connections)
    return cheapest_path


def main():
    input_list: List[Flight] = [
        ('JFK', 'LAX', 500),
        ('JFK', 'ATL', 150),
        ('ATL', 'SFO', 400),
        ('ORD', 'LAX', 200),
        ('LAX', 'DFW', 80),
        ('JFK', 'HKG', 800),
        ('ATL', 'ORD', 90),
        ('JFK', 'LAX', 500)]

    print(find_cheapest(input_list, "JFK", "LAX", 1))  # should return ('JFK', 'LAX', 430) because of only 1 connection
    print('-'*50)
    print(find_cheapest(input_list, "JFK", "LAX", 3))  # example provided in problem description
    print(find_cheapest(input_list, "JFK", "DKJ", 3))  # example provided in problem description
    

if __name__ == "__main__":
    main()