#include <iostream>
#include <vector>

void usage(){
    std::cout << "./a.out <string> <n>" << std::endl;
}

int main(int argc, char **argv) {

    if(argc != 3){
        usage();
        return 1;
    }

    std::string str = argv[1];
    int cols = str.length();
    int n_rows = std::stoi(argv[2]);
    
    std::vector<std::string> rows(n_rows, std::string(cols, ' '));
    
    int direction = 1; // 1 for increasing direction
    int r = 0;
    for(int i = 0; i < cols; ++i){
        rows[r][i] = str[i];
        if(r == 0){
            direction = 1;
        }
        else if(r == (n_rows-1)){
            direction = -1;
        }
        r = r + (1 * direction);
    }

    for(std::string& row : rows){
        std::cout << row << std::endl;
    }

    return 0;
}