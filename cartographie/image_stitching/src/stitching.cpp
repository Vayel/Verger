/*
https://github.com/Itseez/opencv/blob/master/samples/cpp/stitching.cpp

g++ prog.cpp -o dir/binprog `pkg-config --cflags --libs opencv`
*/

#include <iostream>
#include <fstream>
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/stitching/stitcher.hpp"

bool try_use_gpu = false;
std::vector<cv::Mat> imgs;
std::string result_name = "result.png";

void printUsage();
int parseCmdArgs(int argc, char** argv);

int main(int argc, char* argv[]) {
    int retval = parseCmdArgs(argc, argv);
    if(retval) return -1;

    cv::Mat pano;
    cv::Stitcher stitcher = cv::Stitcher::createDefault(try_use_gpu);
    cv::Stitcher::Status status = stitcher.stitch(imgs, pano);

    if(status != cv::Stitcher::OK) {
        std::cout << "Can't stitch images, error code = " << int(status) << std::endl;
        return -1;
    }

    cv::imwrite(result_name, pano);
    
    return 0;
}


void printUsage() {
    std::cout << "my_stitching src1 src2 [...srcN] --output filepath";
}


int parseCmdArgs(int argc, char** argv) {
    if(argc == 1) {
        printUsage();
        return -1;
    }
    
    for(int i = 1; i < argc; ++i) {
        if(std::string(argv[i]) == "--help" || std::string(argv[i]) == "/?") {
            printUsage();
            return -1;
        }
        else if(std::string(argv[i]) == "--try_use_gpu") {
            if(std::string(argv[i + 1]) == "no")
                try_use_gpu = false;
            else if(std::string(argv[i + 1]) == "yes")
                try_use_gpu = true;
            else {
                std::cout << "Bad --try_use_gpu flag value\n";
                return -1;
            }
            i++;
        }
        else if(std::string(argv[i]) == "--output") {
            result_name = argv[i + 1];
            i++;
        }
        else {
            cv::Mat img = cv::imread(argv[i]);
            if(img.empty()) {
                std::cout << "Can't read image '" << argv[i] << "'\n";
                return -1;
            }
            imgs.push_back(img);
        }
    }
    return 0;
}
