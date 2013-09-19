#include<iostream>
using namespace std;

int summ(int a; int b){
	a=a+b;
	cout<<"Summ:"<<a<<endl;
	return a;
}

int main(){
	int a,b,c;
	cout<<"Pleas enter fist number:"<<endl;
	cin>>a;
	cout<<"Pleas enter second number:"<<endl;
	cin>>b;
	c=summ(a,b);
	return 0;
}

//end of homework