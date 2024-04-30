First, I don't know why I did two elif statements when the second one could be an else so I changed the second to an else statement (not technically wrong).
The next next change is to assign self.right.remove(value) to self.right and assign self.right.left(value) to self.left in the elif and else statements.
Next I need to change the entire first if statement. 
First I check to see if self.right == None and if so return self.left. 
Second I check to see if self.left == None and if so return self.right. 
Finally I use an esle statement to do the actual removal. I create a variable called temp and assign it temp = largestValue(self.left) to find a replacement for the node being removed. I then assign temp to self.key. Next i assign self.left = self.left.remove(temp). Finally I return self.

Overall I missed the main part of the function that actual removes the node and replaces the node with the largest value in the left subtree. I did get the part that navigates the tree to find the node to remove with one slight fix.