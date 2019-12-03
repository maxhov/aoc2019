#!/usr/bin/python

orgmem = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,27,13,31,1,31,5,35,1,9,35,39,2,13,39,43,1,43,10,47,1,47,13,51,2,10,51,55,1,55,5,59,1,59,5,63,1,63,13,67,1,13,67,71,1,71,10,75,1,6,75,79,1,6,79,83,2,10,83,87,1,87,5,91,1,5,91,95,2,95,10,99,1,9,99,103,1,103,13,107,2,10,107,111,2,13,111,115,1,6,115,119,1,119,10,123,2,9,123,127,2,127,9,131,1,131,10,135,1,135,2,139,1,10,139,0,99,2,0,14,0]

def add(first, second):
    return first + second


def multiply(first, second):
    return first * second


for noun in range(0,100):
    for verb in range(0,100):
        
        mem = list(orgmem)
        mem[1] = noun
        mem[2] = verb
        
        ip = 0
        for instruction in mem[ip::4]:
            if instruction == 1:
                mem[mem[ip+3]] = add(mem[mem[ip+1]], mem[mem[ip+2]])
                ip += 4
            
            if instruction == 2:
                mem[mem[ip+3]] = multiply(mem[mem[ip+1]], mem[mem[ip+2]])
                ip += 4

            if instruction == 99:
                break
        
        if mem[0] == 19690720:
            print("noun is: " + str(noun) + " and verb is: " + str(verb))
            break
            break

