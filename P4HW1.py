 #Eric Corbett
# 11/08/2024
# P4HW1
# A program that collects scores from the user, validates them, calculates statistics, and assigns a letter grade



def main():
    # Get number of scores from user
    num_scores = int(input("\nHow many scores do you want to enter? "))
    
    # Initialize list for scores
    scores = []
    
    # Collect scores
    for i in range(num_scores):
        while True:
            score = float(input(f'\nEnter score #{i + 1}: '))
            if 0 <= score <= 100:  # Validate score
                scores.append(score)
                break
            else:
                print('\nINVALID Score entered!!!!')
                print('Score should be between 0 and 100')
    
    # Calculate results
    lowest = min(scores)
    modified_scores = scores.copy()
    modified_scores.remove(lowest)
    average = sum(modified_scores) / len(modified_scores)
    
    # Determine letter grade
    if average >= 90:
        letter = 'A'
    elif average >= 80:
        letter = 'B'
    elif average >= 70:
        letter = 'C'
    elif average >= 60:
        letter = 'D'
    else:
        letter = 'F'
    
    # Display results
    print("\n--------------Results--------------")
    print(f'Lowest Score  : {lowest:.1f}')
    print(f'Modified List : {modified_scores}')
    print(f'Scores Average: {average:.2f}')
    print(f'Grade        : {letter}')
    print("----------------------------------")

if __name__ == "__main__":
    main()
