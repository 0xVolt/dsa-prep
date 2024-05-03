// Code by Desh Iyer

// Question:
/*
It's bonus time in the big city! The fatcats are rubbing their paws in anticipation... but who is going to make the most money?

Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.

If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not make enough money and must receive only his stated salary.

Return the total figure the individual will receive as a string prefixed with "£" (= "\u00A3", JS, Go, Java, Scala, and Julia), "$" (C#, C++, Ruby, Clojure, Elixir, PHP, Python, Haskell, and Lua) or "¥" (Rust).

https://www.codewars.com/kata/56f6ad906b88de513f000d96/train/cpp
*/

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

string bonus(int salary, bool bonus) {
    // Create a string stream to construct a string with numeric values
    stringstream output;

    if (bonus) {
        output << "$" << to_string(salary * 10);
        return output.str();
    } else {
        output << "$" << to_string(salary);
        return output.str();
    }
}

string betterBonus(int salary, bool bonus) {
    return (bonus) ? ("$" + to_string(salary * 10)) : ("$" + to_string(salary));
}

int main() {
    cout << betterBonus(100, false);

    return 0;
}