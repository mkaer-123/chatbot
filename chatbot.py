break_point=0.5
import wikipedia
import webbrowser
import time
import random
print("BOT:starting up")
time.sleep(0.7)
print("BOT:importing libarys")

def doge_blocgame():
    import pygame
    import random

    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 480, 640
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dodge the Falling Blocks")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PLAYER_COLOR = (50, 200, 50)
    BLOCK_COLOR = (200, 50, 50)

    # Player properties
    player_width = 60
    player_height = 20
    player_x = WIDTH // 2 - player_width // 2
    player_y = HEIGHT - player_height - 10
    player_speed = 7

    # Block properties
    block_width = 50
    block_height = 30
    block_speed = 5
    blocks = []

    # Game variables
    score = 0
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    def create_block():
        x = random.randint(0, WIDTH - block_width)
        y = -block_height
        return pygame.Rect(x, y, block_width, block_height)

    # Main game loop
    running = True
    while running:
        clock.tick(60)
        screen.fill(WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        # Add new blocks
        if random.random() < 0.02:
            blocks.append(create_block())

        # Move blocks
        for block in blocks[:]:
            block.y += block_speed
            if block.y > HEIGHT:
                blocks.remove(block)
                score += 1

        # Draw player
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

        # Draw blocks
        for block in blocks:
            pygame.draw.rect(screen, BLOCK_COLOR, block)

        # Collision detection
        for block in blocks:
            if player_rect.colliderect(block):
                running = False

        # Draw score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    # Game over
    screen.fill(WHITE)
    game_over_text = font.render("Game Over!", True, BLOCK_COLOR)
    final_score_text = font.render(f"Final Score: {score}", True, BLACK)
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 40))
    screen.blit(final_score_text, (WIDTH//2 - final_score_text.get_width()//2, HEIGHT//2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()


    def print_start():
        current_time = time.strftime("%H:%M:%S", time.localtime())
        
        print("---"+current_time+"---")

def num_gusesser():
    
    print("BOT:Welcome to the Number Guessing Game!")
    
    print("BOT:I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    
    max_attempts = 10  # Limit the number of guesses
    
    while attempts < max_attempts:
        try:
            
            guess = int(input(f"BOT:Attempt {attempts + 1}/{max_attempts}: Take a guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("BOT:Too low! Try again.")
            
            elif guess > secret_number:
                print("BOT:Too high! Try again.")
            
            else:
                print(f"BOT:Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break
        
        except ValueError:
            print("BOT:Invalid input. Please enter a valid number.")
    
    if attempts == max_attempts and guess != secret_number:
        print(f"BOT:Sorry, you've used all {max_attempts} attempts. The number was {secret_number}. Better luck next time!")

    

def greating():
    print("BOT:how is your day")
    day=input("user:")
    
    if day=="good":
        print("BOT:mine to")
    
    elif day=="bad":
        print("BOT: im sory to hear that")
    
    else:
        print("i can not under stand that")
def wikipeda(wikin):
    
    

    print("ChatPal: This uses Wikipedia.")
    wikipedia.set_lang("en")
    results = wikipedia.search(wikin)
    if not results:
        print("ChatPal: No results found. Please try a different topic or check your spelling.")
        return
    print("ChatPal: Search results:", results)
    # If multiple results, let user pick
    if len(results) > 1:
        print("ChatPal: Which topic do you want?")
        for idx, topic in enumerate(results[:5], 1):
            print(f"  {idx}. {topic}")
        try:
            choice = int(input("Enter the number of your choice (or 1): "))
            if 1 <= choice <= min(5, len(results)):
                topic = results[choice-1]
            else:
                topic = results[0]
        except ValueError:
            topic = results[0]
    else:
        topic = results[0]
    try:
        summary = wikipedia.summary(topic, sentences=2)
        print("\nChatPal: Summary:\n", summary)
        page = wikipedia.page(topic)
        print("\nChatPal: Title:", page.title)
        print("\nChatPal: URL:", page.url)
        print("\nChatPal: Content snippet:\n", page.content[:500])
        print("ChatPal: Was this related to your question?")
        time.sleep(break_point)
        related = input("user:")
        copy = random.randint(100, 999)
        filename = f"{wikin.replace(' ', '_')}_{copy}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Title: {page.title}\nSummary: {summary}\nLink: {page.url}\nSearch asked: {wikin}\nResults: {results}\nRelated: {related}\nContent snippet: {page.content[:500]}")
    except wikipedia.DisambiguationError as e:
        print("ChatPal: That topic is ambiguous. Here are some options:")
        for idx, option in enumerate(e.options[:5], 1):
            print(f"  {idx}. {option}")
        print("ChatPal: Please be more specific.")
    except wikipedia.PageError:
        print("ChatPal: Sorry, the page could not be found. Try another topic.")
    except Exception as ex:
        print(f"ChatPal: An error occurred: {ex}")
    
def code_calange():
    chalenge_num=random.randint(1,3)
    if chalenge_num==2:
        print("BOT: make a python numder gussing game")
    
    else:
        print("BOT: make a chat bot")

def story():
    print("BOT:hears a story")
    story=random.randint(1,5)
    if story==2:
        print("BOT:An old clock showed the future. A boy saw a flood coming and built a dam. He saved the town.")
    
    elif story==3:   
        print("BOT:A girl found a library of lost memories. She returned them to people and made the world happier.")
    
    elif story==4:
        print("BOT:A lonely robot built scrap art. One night, an alien loved his work and became his best friend.")
    
    else:
        print("BOT:A boy had a brush that made paintings real. He painted food, homes, and peace between kingdoms.")


#ai



print("BOT:done")

true=True



print("BOT: new conversation")
print("BOT:hello i am your BOT how may i asist you to day")

def show_menu():
    print("\nBOT: Here are some things you can ask me to do:")
    print("  - hi / Hello: Greet the bot")
    print("  - what can you do: List capabilities")
    print("  - i am fealing lonly / i am fealing bored: Play a game")
    print("  - dodge the block game / block game: Play Dodge the Block game")
    print("  - what time is it / whats the time: Show the current time")
    print("  - game: Play the number guessing game")
    print("  - wed search: Open a web search")
    print("  - python coding chalenge / give me a coding chalenge: Get a coding challenge")
    print("  - tell me a story: Hear a story")
    print("  - rock paper scissors: Play Rock, Paper, Scissors")
    print("  - math quiz: Play a math quiz game")
    print("  - quit / stop / pause: Exit the bot")
    print("  - Or type any topic to search Wikipedia\n")
def rock_paper_scissors():
    print("BOT: Let's play Rock, Paper, Scissors!")
    options = ['rock', 'paper', 'scissors']
    import random
    while True:
        user = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user == 'quit':
            break
        if user not in options:
            print("BOT: Invalid choice. Try again.")
            continue
        bot = random.choice(options)
        print(f"BOT: I chose {bot}.")
        if user == bot:
            print("BOT: It's a tie!")
        elif (user == 'rock' and bot == 'scissors') or (user == 'paper' and bot == 'rock') or (user == 'scissors' and bot == 'paper'):
            print("BOT: You win!")
        else:
            print("BOT: I win!")

def math_quiz():
    print("BOT: Welcome to the Math Quiz!")
    import random
    score = 0
    for i in range(5):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(['+', '-', '*'])
        if op == '+':
            answer = a + b
        elif op == '-':
            answer = a - b
        else:
            answer = a * b
        user = input(f"Question {i+1}: What is {a} {op} {b}? ")
        try:
            if int(user) == answer:
                print("BOT: Correct!")
                score += 1
            else:
                print(f"BOT: Wrong. The answer was {answer}.")
        except ValueError:
            print(f"BOT: Invalid input. The answer was {answer}.")
    print(f"BOT: Quiz finished! Your score: {score}/5")

show_menu()

while(true):
    show_menu()
    userinput = input("user: ")
    if userinput == "quit" or userinput == "stop" or userinput == "pause":
        true = False
    elif userinput == "rock paper scissors":
        rock_paper_scissors()
    elif userinput == "math quiz":
        math_quiz()
    
    elif userinput == "hi" or userinput=="Hello":
        greating()
    
    elif userinput=="what can you do":
        print("BOT:ask me any thing you want")
    
    elif userinput=="i am fealing lonly" or userinput=="i am fealing bored" :
        print("BOT:ok lets pass the time by playing a game")
        yes_no=input()
        if yes_no=="no":
            print("BOT:ok")
    
    elif userinput=="dodge the block game" or userinput=="block game":
        doge_blocgame()
   
    elif userinput=="what time is it" or userinput=="whats the time" :
        def print_start():
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print("---"+current_time+"---")
        print_start()
    
    elif userinput=="game":
        print("BOT:sure")
        #number gussing game
        num_gusesser()
    
    elif userinput=="wed search":
        print("BOT:what do you want to search")
        time.sleep(break_point+0.5)
        search=input("user:")
        webbrowser.open(search)
        
    elif userinput=="python coding chalenge" or userinput=="give me a coding chalenge":
        code_calange()
    
    elif userinput=="tell me a story":
        story()
    
    else:
        wikipeda(userinput) 
