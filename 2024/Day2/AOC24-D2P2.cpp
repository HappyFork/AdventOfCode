/*  Advent of Code 2024
    Day 2 Part 2
    Casey Lee
*/

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

bool safetycheck( std::vector<int>& r, bool fromain = false ){
    bool safe = true;   // Return value
    int ascdesc = 0;    // Ascending or descending check
    size_t trouble = 0; // Where the issue is discovered

    // First, figure out if the report is ascending or descending
    for( size_t i = 1; i < r.size(); i++ ){
        if( r[i]>r[i-1] ) ascdesc++;
        else if( r[i]<r[i-1] ) ascdesc--;
    }
    
    // Then, check the strict safety of this report
    if( ascdesc > 0 ){  // If the list is ascending,
        for( size_t i = 1; i < r.size(); i++ ){
            // If any part of the list descends or differs by more than 3
            if( r[i]<=r[i-1] || r[i]-r[i-1]>3 ){
                safe = false;   // Set safe to false
                trouble = i;    // Track where error arose
                break;          // Exit for loop
            }
        }
    } else if( ascdesc < 0 ){   // If the list is descending
        for( size_t i = 1; i < r.size(); i++ ){
            // If any part of the list ascends or differs by more than 3
            if( r[i]>=r[i-1] || r[i-1]-r[i]>3 ){
                safe = false;   // Set safe to false
                trouble = i;    // Track where error arose
                break;          // Exit for loop
            } 
        }
    } else{
        // This should never happen
        safe = false;
    }

    // If it's strictly safe or we're already testing the second level, return
    if( safe || !fromain ) return safe;
    else{   // Otherwise, make altered reports to re-test
        std::vector<int> temp(r);

        // First, test by deleting the front
        temp.erase( temp.begin() );
        if( safetycheck(temp) ) return true;
        temp = r;   // Copy r again if it didn't work

        // Second, test by deleting the back
        temp.erase( temp.end() - 1 );
        if( safetycheck(temp) ) return true;
        temp = r;   // Copy r again if it didn't work

        // Trouble at 0 means we don't know where else to check
        if( trouble == 0 ) return false;

        if( (trouble-1)!=0 ){    // If we're not repeating ourself,
            // Test by deleting before trouble
            temp.erase( temp.begin() + (trouble-1) );
            if( safetycheck(temp) ) return true;
        }
        temp = r;   // Copy r again if it didn't work

        // Test by deleting at trouble
        temp.erase( temp.begin() + trouble );
        if( safetycheck(temp) ) return true;
        temp = r;   // Copy r again if it didn't work

        if( (trouble+1) < r.size() ){  // Stay in bounds
            temp.erase( temp.begin() + (trouble+1) );
            if( safetycheck(temp) ) return true;
        }

        return false;
    }
}

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

    std::string line = "";
    int answer = 0;
    getline( file, line );
    while( !file.eof() ){
        std::stringstream ss( line );
        std::vector<int> report;
        // I'm reusing line here bc I don't want to make a new string
        // and it doesn't matter what I do with line inside the loop
        while( ss >> line ) report.push_back( stoi(line) );

        // Check to see if the report is safe
        if( safetycheck(report, true) ) answer++;
        getline( file, line );
    }

    std::cout << answer << std::endl;
    return 0;
}