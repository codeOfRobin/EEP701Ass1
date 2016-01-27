#include <iostream>
#include <stdlib.h>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
float difference(int a[4][4], int b[4][4])
{
    float sum = 0;
    for(int i = 0; i<4 ; i++)
    {
        for(int j=0 ;j<4 ; j++)
        {
             sum+= (a[i][j] - b[i][j])*(a[i][j] - b[i][j]);
        }
    }
    return sum;
}

int allsols[288][4][4];

void importSudokus()
{
    std::string line;

    std::fstream myfile ("filename.csv");
    int lineNum = 0;
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
            std::vector<int> vect;
            std::stringstream ss(line);
            int i;
            int counter = 0;
            while (ss >> i)
            {
                vect.push_back(i);
                allsols[lineNum/4][lineNum%4][counter] = i;
                counter++;
                if (ss.peek() == ',')
                    ss.ignore();
            }
            lineNum++;
        }
        myfile.close();
    }
    else std::cout << "Unable to open file";

}
int main()
{
    int initial[4][4] = {{1,3,1,4},{1,4,3,2},{2,3,1,4},{1,3,2,4}};
    importSudokus();
    int minSudIndex = 0;
    int minDiff = 2000;
    for(int i=0;i<288;i++)
    {
        if(difference(initial,allsols[i])<minDiff)
        {
            
            // std::cout<<difference(initial,allsols[i])<<"\n";
            minDiff = difference(initial,allsols[i]);
            minSudIndex = i;
        }
    }
    std::cout<<minSudIndex<<'\n';
    std::cout<<difference(initial,allsols[minSudIndex]);
    return 0;
}