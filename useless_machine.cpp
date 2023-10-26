#include <iostream>
#include <windows.h>
#include <stdlib.h>
#include <time.h>
int main(){

	srand(time(NULL));

	int seconds = rand() % 5 + 1;
	int times = rand() % 20 + 1;

	Sleep(5000);

	while(true){
		for(int i = 0; i < times; i++){
			keybd_event(VK_BACK, 0, 0, 0);
			keybd_event(VK_BACK, 0, KEYEVENTF_KEYUP, 0);
		}
	        seconds = rand() % 5 + 1;
	        times = rand() % 20 + 1;
		Sleep(seconds*1000);
	}
	return 0;
}
