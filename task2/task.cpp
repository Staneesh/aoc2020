#include <iostream>

using namespace std;

int main()
{
	int ln = 0;
	int valid = 0;
	while (true)
	{
		int low;
		int hi;
		char letter;
		string pass;
		int occ = 0;

		char minus, colon;
		if (cin>>low)
		{
			cin>>minus>>hi>>letter>>colon>>pass;
			/* part1
			for (auto c: pass)
			{
				if (c == letter)
				{
					++occ;
				}

				
			}
			if (occ >= low && occ <= hi)
			{
				++valid;
			}
			*/

			if ((pass[low-1] == letter)^(pass[hi-1] == letter))
			{
				++valid;
				cout<<"found: "<<low<<"-"<<hi<<" ("<<letter<<"): "<<pass<<endl;
			}
		}
		else
		{
			break;
		}

		ln++;
	}

	cout<<ln<<endl;
	cout<<"valid: "<<valid<<endl;
	return 0;	
}
