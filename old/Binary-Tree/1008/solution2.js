
const bstFromPreorder = (preorder) => {
  const inorder = preorder.map(item => item).sort((a, b) => a - b);

  return buildTree(preorder, inorder);
}

const buildTree = (preorder, inorder) => {
  if (preorder.length === 0) {
    return null;
  }

  const rootValue = preorder.shift();

  const root = new TreeNode(rootValue);

  const index = inorder.indexOf(rootValue);

  root.left = buildTree(preorder.slice(0, index), inorder.slice(0, index));
  root.right = buildTree(preorder.slice(index), inorder.slice(index + 1));

  return root;
}