'''
it's a simple reflex agent which means these kind of agents acts only based on the current situation and
these agents don't have any memory and they don't plan/reason anything and they just follow if-else rules 
.This simple reflex agent will check if the current room is dirty then it will clean the room otherwise 
it will move to another room.'''
'''Logic:- Agent will get 8 turns(8 steps)
Each "step" (one cycle where the agent):
1. Check current room (Perceives)
2. Decides what to do (Reasons)
3. Perform the action (Act)
4. Update the environment 
In all the 8 steps it will do these 4 things
At each step agent will only go in one room. So, if there are 4 rooms and 8 steps, then all the room will
be checked 2 times. if suppose the 2nd room is dirty and all the other rooms are clean , then at step 2 and step 6 the agent will be at room no 2
but as simple reflex agent doesn't have any memory then how does it knows that it doesn't have to clean the room no 2 because it must have been cleaned 
at step 2 ? it's bcoz even though it doesn't have memory to remember, but each step has the last step as updating the environment. So, after step 2 the
environment have been updated to clean after each step. So room no 2 will be marked as clean in the environment, so when the agent comes back to room2 then
it sees that the room is clean,so it moves forward.
'''
import random, matplotlib 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

# Define the 2*2 environment dictionary

environment = {
    "Room1":"Clean",
    "Room2": "Dirty",   #Start with dirt here
    "Room3": "Clean",
    "Room4": "Clean"
}

#Mapping for grid positions
room_positions = {
    "Room1": (0,1), #Top left
    "Room2": (1,1), #Top right
    "Room3": (0,0), #Bottom left
    "Room4": (1,0)  #Bottom right
}

rooms = list(environment.keys()) # in rooms I created a list of room environment keys i.e., [Room1, Room2, Room3, Room4]. Create a list of all room names from the environment dictionary
agent_index = 0 # means the agent will start in Room1

#Defining a reflex agent function with parameter as state
def reflex_agent(state):
    if state == "Dirty":
        return "Clean"
    else:
        return "Move"
# Function to Draw the Grid
def draw_environment(env, agent_pos, step):
    fig, ax= plt.subplots()
    ax.set_xlim(0, 2)     #first two lines will give us 2*2 grids i.e., 2 rows and 2 columns
    ax.set_ylim(0, 2)
    ax.set_xticks ([])    #these two lines will remove the x from x_axis and y from y_axis
    ax.set_yticks ([])
    ax.set_title (f"Step {step}- Agent in {rooms[agent_pos]}")  # this line will show the title on each grid

    for room, pos in room_positions.items():
        x,y = pos
        color = 'red' if env[room]== 'Dirty' else 'green'  #if room is dirty then color it red otherwise color it green
        rect = patches.Rectangle ((x, y ), 1, 1, facecolor=color, edgecolor = 'black') # it puts a rectangle of red color if room is dirty otherwise it puts rectangle of black color if room is dirty
        ax.add_patch(rect)
        ax.text (x + 0.5, y + 0.5, room, ha= 'center' , va = 'center', color = 'white', fontsize='10') # with the ax.text we are writing the room number in the center of each reactangle

    # Draw agent
    agent_x, agent_y = room_positions [rooms[agent_pos]] # Finds the agent's current position
    agent_patch= patches.Circle((agent_x + 0.5, agent_y+ 0.5), 0.1, color='blue') # makes a blue circle which depicts the agent
    ax.add_patch(agent_patch)

    plt.pause(2)  # this pause says wait for 2 secs after reaching each room
    plt.show(block=False)   # this means move to the next step

# Run simulation
plt.ion()   #ion means interaction mode on. Reason for ion is bcoz we are running the code for 8 steps and after each step we want to visualize the results and see where our agent is live on the screen
steps = 8   # agent will take 8 turns and each step will focus on 1 room only

for step in range(steps):
    current_room = rooms[agent_index]    # this will give the current room the agent is in because rooms is a dictionary which starts from index 0 : [Room 1,Room2, Room3, Room4]
    state = environment[current_room]    # this state will keep the environment of current_room i.e., for eg., environment of Room1 is Clean
    action = reflex_agent(state)         # this will call the reflex_agent function which runs the simple if, else statement i.e., if room is clean then it moves forward and if room is dirty then it cleans the room

    draw_environment(environment, agent_index, step+1) # calls the draw_environment funtion which will draw the the diagram again for next step, it will be helpful in full visualization in all the steps. Here step is incremented by 1

    if action == "Clean":  # if the agent decides to clean a dirty room, this line updates the environment, marking the room as "Clean".
        environment[current_room] = "Clean"     # when the action is clean then the environment of the current room is changed to clean from dirty
    else:
        agent_index = (agent_index+1) % len(rooms)     # modulus operator ensures the index wraps around, i.e., after Room 4 it comes to Room 1 again.

'''| Current `agent_index` | After `+1` | After `% 4` | Final              |
   | --------------------- | ---------- | ----------- | ------------------ |
   | 0                     | 1          | 1           | Room2              |
   | 1                     | 2          | 2           | Room3              |
   | 2                     | 3          | 3           | Room4              |
   | 3                     | 4          | 0           | Room1 (wraps back) |
'''

plt.ioff()
print(" Simulation complete")