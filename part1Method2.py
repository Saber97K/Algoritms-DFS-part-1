from collections import deque

def search_rooms(matrix, current_position, visited_positions, visited_rooms):
    x, y = current_position
    rows, cols = len(matrix), len(matrix[0])
    
    # Create a queue for BFS traversal
    queue = deque()
    queue.append(current_position)
    


    # Check if the current position has already been visited or is not a room block
    if current_position in visited_positions:
        return
    
    # Mark the starting position as visited
    visited_positions.append(current_position)
    
    room_names = {
        -1: "Stairs 1" ,
        -2: "Stairs 0",
        1: "Entrance",
        2: "Main Hall",
        3: "Utility",
        4: "Dining",
        5: "Kitchen",
        6: "Courtyard",
        7: "Library",
        8: "Balcony",
        9: "Room 1",
        10: "Void",
        11: "Room 3",
        12: "Room 2",
        13: "Master Bedroom"
    }


    while queue:
        current_position = queue.popleft()
        x, y = current_position

        room_value = matrix[x][y]
        if room_value != 0:
            room_name = room_names.get(room_value, "Empty")
            visited_rooms.append((current_position, room_name))

        # Check if the current position is the upstairs zone (-1 or -2)
        if room_value == -1 or room_value == -2:
            # Transition to the second floor matrix
            second_floor_matrix = [
                [-2,  9,  0, 10, 10, 10,  0, 11, 11, 8],
                [-2,  9,  0, 10, 10, 10,  0, 11, 11, 8],
                [-2,  9,  0, 10, 10, 10,  0, 12, 12, 8],
                [ 0,  0,  0,  0,  0,  0,  0, 12, 12, 8],
                [ 3, 13, 13, 13, 13, 13, 13, 12, 12, 8],
                [ 3, 13, 13, 13, 13, 13, 13, 12, 12, 8],
                [ 8,  8,  8,  8,  8,  8,  8,  8,  8, 8]
                # Add the matrix representation of the second floor here
            ]
            # Starting position on the second floor
            second_floor_starting_position = (0, 0)
            
            # Perform BFS on the second floor
            search_rooms(second_floor_matrix, second_floor_starting_position , visited_positions_2 , visited_rooms)

        # Explore all adjacent blocks
        adjacent_positions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for position in adjacent_positions:
            x, y = position
            
            # Check if the adjacent position is within the matrix bounds
            if 0 <= x < rows and 0 <= y < cols and position not in visited_positions:
                queue.append(position)
                visited_positions.append(position)

    return visited_rooms


# Matrix representation of the building
matrix = [
    [-1, 7, 7, 6, 6, 6, 0, 5, 5, 8],
    [-1, 7, 7, 6, 6, 6, 0, 5, 5, 8],
    [-1, 7, 7, 6, 6, 6, 0, 4, 4, 8],
    [ 0, 0, 0, 0, 0, 0, 0, 4, 4, 8],
    [ 3, 2, 2, 2, 2, 2, 2, 4, 4, 8],
    [ 3, 2, 2, 2, 2, 2, 2, 4, 4, 8],
    [ 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]

# Starting position (entrance of the main building)
starting_position = (6, 4)

# List to store visited positions
visited_positions = []
visited_rooms = []
visited_positions_2 = []

# Search all the rooms in the building
search_rooms(matrix, starting_position, visited_positions, visited_rooms)

print("Visited Positions:", visited_rooms)
