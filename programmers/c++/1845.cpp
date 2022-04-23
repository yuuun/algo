#include <set>
#include <vector>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    set<int> tmp;
    for (int i = 0; i < nums.size(); i++){
        tmp.insert(nums[i]);
    }
    answer = tmp.size();
    int pick = nums.size() / 2;
    if (answer > pick){
        answer = pick;
    }
    return answer;
}