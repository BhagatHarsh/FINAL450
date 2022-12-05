
//link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

/*
The trick was to stick with the minimum value until you find another smaller value
till then subtract the other prices and get the maximum profit
*/

class Solution {
  int maxProfit(List<int> prices) {
      int n = prices.length;
      int lastMin = 0;
      int maxProf = 0;
      for(int i=0;i<n;++i){
          if(prices[lastMin] < prices[i]){
              maxProf = max(maxProf, prices[i] - prices[lastMin]);
          }else{
              lastMin = i;
          }
      }
      return maxProf;


//Failed approach
//     int n = prices.length;
//     int minInd = n;
//     int maxVal = -1;
//     int minVal = 1000000;
    
//     for(int i=0;i<n;++i){
//         if(prices[i] < minVal)
//         {
//             minVal = prices[i];
//             minInd = i;
//         }
//     }
//     int maxInd = minInd;
//     if(minInd != n){
//         for(int i=minInd+1;i<n;++i){
//             if(prices[i]>maxVal){
//                 maxVal = prices[i];
//                 maxInd = i;
//             }
//         }
//     }
//     if(minInd < maxInd){
//         return maxVal - minVal;
//     }else{
//         return 0;
//     }
  }
}


