#include <iostream>
#include <windows.h>
#include <cmath>

int main(){

	//Time it takes for each catch in seconds. Will average out numbers.
	
	double catches[10] = {3.19, 3.05, 4.70, 3.38, 2.50, 2.95, 3.28, 2.87, 3.18, 3.05};

	double n = 0;
	//cursor coordinates
	int x = 500;
	int y = 500;
	int size = sizeof(catches) / sizeof(catches[0]);
	for(int i = 0; i < size; i++){
		n += catches[i];
	}

	n = floor(n / size);

	int times;
	std::cout<<"Enter the amount of times you want to fish for: ";
	std::cin>>times;

	for(int i = 5; i >= 1; i--){
		std::cout<<i<<"\n";
		Sleep(1000);
	}
	std::cout<<"started";	

	for(int i = times; i >= 1; i--){

		mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0);
		Sleep(250);
		mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
		Sleep((n*1000)-300);
		mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
		Sleep(250);
		mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
		Sleep(250);
		std::cout<<i-1<<" more iterations.";
	}

	return 0;
}
