class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string s="";

        int index = 0;
        while(index < strs[0].size()){
            char c = strs[0][index];
            bool flag = false;
            for(int i=0; i < strs.size() ; i++){
                if(index >= strs[i].size()) return s;

                if(strs[i][index] == c){
                    flag = true;
                }
                else{
                    flag = false;
                    return s;
                }
                
            }
            if(flag){
                s+=c;
            }
            index++;
        }
        return s;
    }
};