#include<iostream>
using namespace std;

struct node
{
    int data;
    node *left;
    node *right;

    node(int data)
    {
        this -> data = data;
        left = NULL;
        right = NULL;
    }
};

node *create_tree()
{
    node *root = new node(15);

    root ->left = new node(17);
    root ->left->left = new node(19);
    root ->left -> right = new node(20);
    root ->left -> right -> left = new node(10);
    root ->left -> right -> right = new node(9);
    root ->left -> right -> right -> left = new node(8);
    root ->left -> right -> right -> left -> left = new node(6);
    root ->left -> right -> right -> left -> right = new node(5);
    root ->left -> right -> right -> right = new node(7);
    root ->left -> right -> right -> right -> left = new node(17);
    root ->left -> right -> right -> right -> right = new node(20);

    root ->right = new node(18);
    root ->right -> left = new node(7);
    root ->right -> right = new node(14);
    root ->right -> right -> left = new node(19);
    root ->right -> right -> left -> left = new node(6);
    root ->right -> right -> left -> right = new node(2);
    root ->right -> right -> left -> right -> left = new node(3);
    root ->right -> right -> left -> right -> right = new node(4);
    root ->right -> right -> right = new node(21);
    root ->right -> right -> right -> left = new node(4);
    root ->right -> right -> right -> right = new node(2);
    root ->right -> right -> right -> right -> left = new node(3);
    root ->right -> right -> right -> right -> right = new node(7);


    return root;
}

void inorder(node *root)
{
    if(root == nullptr)
    {
        return;
    }
    inorder(root -> left);
    cout<<root -> data<<" ";
    inorder(root -> right);

}

void preorder(node *root)
{
    if(root == nullptr)
    {
        return;
    }
    cout<<root -> data<<" ";
    preorder(root -> left);
    preorder(root -> right);

}

void postorder(node *root)
{
    if(root == nullptr)
    {
        return;
    }
    postorder(root -> left);
    postorder(root -> right);
    cout<<root -> data<<" ";

}


int main()
{
    node *root = create_tree();
    
    cout<<"INORDER: ";
    inorder(root);
    cout<<"\n";

    cout<<"PREORDER: ";
    preorder(root);
    cout<<"\n";

    cout<<"POSTORDER: ";
    postorder(root);

    return 0;
}