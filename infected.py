from collections import deque

def num_infected(initial_infected: str, user_map: dict[str, list[str]]) -> int:
    """
    Given the initial infected user and a map of which user got the 
    UltraSheet from which other user, returns the total number of 
    infected users.
    Precondition: initial_infected is a string. user_map is a 
    dictionary mapping strings to lists of strings.
    """
    # Set to keep track of infected users
    infected_users = set()
    
    # Queue to perform BFS
    queue = deque([initial_infected])
    
    while queue:
        current_user = queue.popleft()
        infected_users.add(current_user)
        
        if current_user in user_map:
            for infected_by in user_map[current_user]:
                if infected_by not in infected_users:
                    queue.append(infected_by)
    
    return len(infected_users)
