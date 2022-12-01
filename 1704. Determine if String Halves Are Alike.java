class Solution {
    public boolean halvesAreAlike(String s) {
        int len = s.length();
        String a = s.substring(0, len/2); // First Half
        String b = s.substring(len/2, len); // Second Half
        int ctr1 = countVowels(a); // Number of vowels present in first half
        int ctr2 = countVowels(b); // Number of vowels present in second half
        if(ctr1 == ctr2) // Checking if the count is same
            return true;
        else return false;
    }
    
    private static int countVowels(String s) { // To count the number of vowels
        int count = 0;
        for(int i = 0;i < s.length();i++) {
            char ch = s.charAt(i);
            if(ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U' ||ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
                count++;
        }
        return count;
    }
}
-----------------------------------------------------------------------------------------------------------------------------------------------------------
