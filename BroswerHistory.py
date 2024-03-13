from queue import LifoQueue
backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None
#visit format
NoOfvisits = int(input("Enter the number of URL history"))
print("Enter the URLs to vosit")
for i in range(NoOfvisits):
    url = input("URL:")
    print(f"visiting {url}")
    backward_history.put(current_page)
    current_page = url
    #display current page
    print(f"Current page: {current_page}")
    #go back
while input("Do you want to go back? (yes/no): ").lower() == 'yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page = backward_history.get()
        print(f"Going back to {current_page}")
    else:
        print("No previous page available")
    #go forward
while input("Do you want to forward? (yes/no): ").lower() == 'yes':
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"Going forward to {current_page}")
    else:
        print("No forward page available")