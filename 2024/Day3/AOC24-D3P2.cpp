/*  Advent of Code 2024
    Day 3 Part 2
    Casey Lee
*/

#include <fstream>
#include <iostream>
#include <string>

int main( int argv, char* argc[] ){
    if( argv != 2 ){
        std::cout << "Give me a file, stupid." << std::endl;
        return 1;
    }

    std::ifstream file( argc[1] );
    if( !file ){
        std::cout << "Give me a real file, stupid." << std::endl;
        return 1;
    }

    int answer = 0;
    const std::string key = "on'tul";
    std::string p1 = "", p2 = "", inst = "";
    bool toggle = true, collecting = false;
    char c;
    while( !file.get(c).eof() ){
        if( c == 'd' || c == 'm' ){
            // Start a new instruction no matter what
            collecting = true;
            p1 = "";
            p2 = "";
            inst = "";
            inst += c;
            continue;
        }

        // Ok this is probably really inefficient, but this
        // helps me avoid extracting the beggining of an
        // instruction after a malformed mul(X,X)
        if( inst == "mul(" ){
            if( collecting && c >= '0' && c <= '9' ) p2 += c;
            else if( !collecting && c >= '0' && c <= '9' ) p1 += c;
            else if( !collecting && c == ',' ) collecting = true;
            else if( collecting && c == ')' ){
                // End of instruction. Add product to answer
                answer += ( stoi(p1)*stoi(p2) );
                // Reset variables
                p1 = "";
                p2 = "";
                inst = "";
                collecting = false;
            } else{
                // If ANYTHING unexpected happens, reset it all
                p1 = "";
                p2 = "";
                inst = "";
                collecting = false;
            }
            continue;
        }

        if( collecting && c == '(' ){
            // Figure out the instruction
            if( toggle && inst == "mul" ){
                // mul(X,X)
                // set up the wacky stuff above
                inst += c;
                collecting = false;
                //continue;
            } else{
                // don't()
                if( toggle && inst == "don't" && file.peek() == ')' ) toggle = false;
                // do()
                else if( !toggle && inst == "do" && file.peek() == ')' ) toggle = true;
                // Reset all variables
                p1 = "";
                p2 = "";
                inst = "";
                collecting = false;
            }
        } else if( collecting && key.find( c ) == std::string::npos ){
            // If the character doesn't continue an instruction, reset
            collecting = false;
            inst = "";
        } else if( collecting ) inst += c;
    }

    std::cout << answer << std::endl;
    return 0;
}