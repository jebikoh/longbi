#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct TrieNode {
  struct TrieNode* children[26];
  bool is_word;
} TrieNode;

TrieNode* create_node() {
  TrieNode* node = malloc(sizeof(TrieNode));
  node->is_word = false;
  for (int i = 0; i < 26; ++i) {
    node->children[i] = NULL;
  }
  return node;
}

void free_trie_node(TrieNode* root) {
  if (root == NULL) return;

  for (int i = 0; i < 26; ++i) {
    if (root->children[i] != NULL) {
      freeTrie(root->children[i]);
    }
  }

  free(root);
}

int index_of(char c) { return c - 'A'; }

bool has_child(TrieNode* node, char c) {
  return node->children[index_of(c)] != NULL;
}

TrieNode* get_child(TrieNode* node, char c) {
  TrieNode* child = node->children[index_of(c)];
  return child;
}

void set_child(TrieNode* node, char c, TrieNode* child_node) {
  node->children[index_of(c)] = child_node;
}

typedef struct Trie {
  TrieNode* root;
} Trie;

Trie* create_trie() {
  Trie* trie = malloc(sizeof(Trie));
  trie->root = create_node();
  return trie;
}

void free_trie(Trie* trie) {
  free_trie_node(trie->root);
  free(trie);
}

void insert(Trie* trie, const char* word) {
  TrieNode* node = trie->root;
  for (int i = 0; i < strlen(word); ++i) {
    if (!has_child(node, word[i])) {
      set_child(node, word[i], create_node());
    }
    node = get_child(node, word[i]);
  }
  node->is_word = true;
}

bool search(Trie* trie, const char* word) {
  TrieNode* node = trie->root;
  for (int i = 0; i < strlen(word); ++i) {
    if (!has_child(node, word[i])) {
      return false;
    }
    node = get_child(node, word[i]);
  }
  return node->is_word;
}

int main() {
  Trie* trie = create_trie();

  insert(trie, "APPLE");
  insert(trie, "APP");

  printf("Search APP: %d\n", search(trie, "APP"));
  printf("Search APPLE: %d\n", search(trie, "APPLE"));
  printf("Search APPL: %d\n", search(trie, "APPL"));

  free_trie(trie);

  return 0;
}