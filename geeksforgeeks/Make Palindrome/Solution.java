
class Solution {
    public static boolean makePalindrome(int n, String[] arr) {
        // code here
        HashMap<String,Integer> obj=new HashMap<>();
        for(int i=0;i<n;i++)
        {
            StringBuffer sb=new StringBuffer();
            sb.append(arr[i]);
            String temp=sb.reverse().toString();
            if(obj.containsKey(temp))
            {
                obj.put(temp,obj.get(temp)-1);
                if(obj.get(temp)==0)
                {
                    obj.remove(temp);
                }
            }
            else if(obj.containsKey(arr[i]))
            {
                obj.put(arr[i],obj.get(arr[i])+1);
            }
            else
            {
                obj.put(arr[i],1);
            }
        }
        //System.out.println(obj);
        if(obj.size()==0)
        {
            return true;
        }
        else if(obj.size()==1)
        {
            StringBuffer sb=new StringBuffer();
            for(String key:obj.keySet())
            {
                if(obj.get(key)>1)
                {
                    return false;
                }
                sb.append(key);
            }
            return sb.toString().equals(sb.reverse().toString());
        }
        return false;
    }
    
}
