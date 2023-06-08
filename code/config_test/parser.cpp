#include <iostream>
#include <fstream>
#include <regex>
#include <string>
#include <vector>
#include <fstream>

using namespace std;
int main() {
    std::ifstream file("cat_all_raw.html"); // Podaj nazwę pliku HTML
    std::ofstream outputFile("my_categories.txt"); // Podaj nazwę pliku wyjściowego, do którego chcesz zapisać linie
    std::vector<string> categories;
    if (file.is_open()) {
        std::string line;
        std::regex tagRegex(R"(<a.*?title=\"Tag:([^\"]+)\">.*?</a>)");
        std::regex dataTagRegex(R"(data-taginfo-taglist-tags=\"([^\"]+)\")");
        // std::regex classRegex(R"(<h3><span class=\"mw-headline\" id=\"([^\"]+)\">)");

        while (std::getline(file, line)) {
            std::smatch tagMatch, classMatch, dataTagMatch;

            if (std::regex_search(line, tagMatch, tagRegex)) {
                std::string tag = tagMatch[1].str();
                if (tag == "type=site") continue;
                // std::cout << tag << std::endl;
                outputFile << tag << std::endl;
            }

            //UWAZAJ NA dyke
            if (std::regex_search(line, dataTagMatch, dataTagRegex)) {
                std::string dataTags = dataTagMatch[1].str();
                outputFile << "data-taginfo-taglist-tags: " << dataTags << std::endl;
            }
            

            // if (std::regex_search(line, classMatch, classRegex)) {
            //     std::string category = classMatch[1].str();
            //     std::cout << "Znaleziono pasującą kategorię: " << category << std::endl;
            // }
        }

        file.close();
        outputFile.close();
    } else {
        std::cout << "Nie można otworzyć pliku." << std::endl;
    }

    return 0;
}
