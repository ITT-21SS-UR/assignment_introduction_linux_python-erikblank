import math
import sys

def read_numbers():
    arg_len = len(sys.argv)
    
    if arg_len == 1:
        numbers = input("Type in numbers seperated by space: ")
        return numbers
    if arg_len == 2:
        numbers = open(sys.argv[1]).readlines()
        return numbers
    else: 
        print("invalid input")
        sys.exit(1)
        
def main_func():
    input_numbers = read_numbers()
    numbers = numbers_to_arr(input_numbers)
    print("Mean: " + str(calc_mean(numbers)))
    print("Median: " + str(calc_median(numbers)))
    print("Deviation: " + str(calc_deviation(numbers)))
    
def numbers_to_arr(input_numbers):
    if isinstance(input_numbers, list):
        input_numbers = input_numbers[0]
        

    numbers = input_numbers.replace(",", ".").split(" ")

    for i in range(len(numbers)):
        numbers[i] = float(numbers[i])

        
    return numbers

def calc_mean(numbers):
    return sum(numbers)/len(numbers)

def calc_median(numbers):
    sorted_numbers = sorted(numbers)
    index = (len(numbers) -1) // 2
    
    if(len(numbers) % 2):
        return sorted_numbers[index]
    else:
        return (sorted_numbers[index] + sorted_numbers[index+1]) / 2.0
    
def calc_deviation(numbers):
    if len(numbers) < 2:
        return "two numbers are need to calculate deviation"
    else:
        return math.sqrt(calc_variance(numbers))
    
    
def calc_variance(numbers):
    mean = calc_mean(numbers)
    deviations = [(num - mean) ** 2 for num in numbers]
    
    return sum(deviations) / (len(numbers) -1)
    

if __name__ == "__main__":
    main_func()
    
    
    