/**
 * A simple hello world program.
 */

 #include <cctype>
 #include <cstdlib>

 #include <algorithm>
 #include <iostream>
 #include <string>

 int main(int argc, char *argv[]) {
    std::string who("world");
    if (argc > 1) {
        who = argv[1];
    } else {
        char *value = std::getenv("USER");
        if (value) {
            who = value;
        }
    }

    std::transform(who.begin(), who.end(), who.begin(), ::tolower);
    if (who.length() > 0) who[0] = std::toupper(who[0]);
    std::cout << "Hello, " << who << " !!!" << std::endl;

    return 0;
 }
