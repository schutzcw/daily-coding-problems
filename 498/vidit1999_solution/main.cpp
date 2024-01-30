#include <bits/stdc++.h>

/*
Given an array of integers out of order, determine the bounds of the smallest window
that must be sorted in order for the entire array to be sorted.
For example, given [3, 7, 5, 6, 9], you should return (1, 3)
*/

std::pair<int ,int> windowRange(std::vector<int> arr){
	int s=0, e=arr.size()-1;
	
	for(;s<arr.size()-2;s++){
		if(arr[s] > arr[s+1])
			break;
	}
    
    // At this point, s is the index of the first value that is greater than the value
    // directly to it's right
	std::cout << "1s: " << s << std::endl;

	if(s == arr.size()-1)
		return {0, 0};
	
	for(;e>=1;e--){
		if(arr[e] < arr[e-1])
			break;
	}

    // At this point, e is the index of the last value that is less than the value to it's
    // right
    std::cout << "1e: " << e << std::endl;
	
	int max = arr[s], min = arr[s];
	
	for(int i=s+1;i<=e;i++){
        std::cout << "i: " << i << ", arr[i]: " << arr[i] << std::endl;
		if(arr[i] > max)
			max = arr[i];
		if(arr[i] < min)
			min = arr[i];
	}
	
	for(int i=0;i<s;i++){
		if(arr[i] > min){
			s = i;
			break;
		}
	}
	
	for(int i=arr.size()-1;i>e;i--){
		if(arr[i] < max){
			e = i;
			break;
		}
	}

	return {s, e};
}

// main function
int main(){
    // [1, 7, 8, 9, 2, 3, 4]
    std::pair<int, int> ans = windowRange({1, 2, 3, 8, 9, 10, 4, 5, 12, 6, 11, 13});
	//std::pair<int, int> ans = windowRange({3, 7, 5, 6, 9});
	std::cout << ans.first << " -- " << ans.second << "\n";
	return 0;
}