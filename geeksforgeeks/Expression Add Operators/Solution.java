class Solution {

    public static void helper(ArrayList<String> ans, String res, String num, int target, int index, long val, long mul) {

        if(index == num.length()) {

            if(val == target) 

                ans.add(res);

                

            return;

        }

        

        for(int i =index; i < num.length(); i++) {

            if(i != index && num.charAt(index) == '0') break;

            long cur = Long.parseLong(num.substring(index, i + 1));

            if(index == 0) {

                helper(ans, res + cur, num, target, i + 1, cur, cur);

            } else {

                helper(ans, res + "+" + cur, num, target, i + 1, val + cur, cur);

                helper(ans, res + "-" + cur, num, target, i + 1, val - cur, -cur);

                helper(ans, res + "*" + cur, num, target, i + 1, val - mul + mul * cur, mul * cur);

            }

        }

    }

    public static ArrayList<String> addOperators(String S, int target) {

        // code here

        

        ArrayList<String> ans = new ArrayList<>();

        if(S.length() == 0 || S == null) return ans;

        helper(ans, "", S, target, 0, 0, 0);

        return ans;

    }

}
