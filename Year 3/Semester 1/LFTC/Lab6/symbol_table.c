#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEXEME 4096

typedef struct Node {
    // IDENTIFIER, CONSTANT
    char type[32];

    // actual text
    char lexeme[MAX_LEXEME];

    // assigned position
    int position;
    struct Node *left;
    struct Node *right;
} Node;

static Node *root = NULL;
static int next_position = 0;

// BST rule organize alphabetically
static int compare_keys(
    const char *type1, const char *lexeme1,
    const char *type2, const char *lexeme2
) {
    // strcmp: - => keep order, 0 => strings are equal, + => first string after second
    int result = strcmp(type1, type2);

    // if the types are different, return their difference
    if (result != 0) {
        return result;
    }

    // if the types are the same, return the difference from the lexemes
    return strcmp(lexeme1, lexeme2);
}

static Node *insert(Node *node, const char *type, const char *lexeme) {
    // if the tree is empty, create the first node
    if (node == NULL) {
        Node *created = malloc(sizeof(Node));

        if (created == NULL) {
            fprintf(stderr, "Memory allocation failed.\n");
            exit(EXIT_FAILURE);
        }

        // copy into created-> type, the type
        snprintf(created->type, sizeof(created->type), "%s", type);

        // same for lexeme
        snprintf(created->lexeme, sizeof(created->lexeme), "%s", lexeme);

        created->position = next_position++;
        created->left = NULL;
        created->right = NULL;

        return created;
    }

    // if tree is not empty
    // compare the current node with the one we want to insert
    int comparison = compare_keys(
        type, lexeme, node->type, node->lexeme
    );

    // keep order: new first, current after
    // => insert the new one on the left side of the tree recursively
    if (comparison < 0) {
        node->left = insert(node->left, type, lexeme);
    }
    // else insert new one on the right
    else if (comparison > 0) {
        node->right = insert(node->right, type, lexeme);
    }

    //Equal keys already exist, so their position is reused.
    return node;
}

// in order traversal
static void print_in_order(Node *node, FILE *output) {
    if (node == NULL) {
        return;
    }

    print_in_order(node->left, output);

    fprintf(
        output, "%d\t%s\t%s\n",
        node->position, node->type, node->lexeme
    );

    print_in_order(node->right, output);
}

// free the allocated memory
static void free_tree(Node *node) {
    if (node == NULL) {
        return;
    }

    free_tree(node->left);
    free_tree(node->right);
    free(node);
}

int main(int argc, char *argv[]) {
    const char *input_name = "symbol_input.txt";

    const char *output_name = "symbol_table.txt";

    FILE *input = fopen(input_name, "r");

    if (input == NULL) {
        perror("Could not open symbol input file");
        return EXIT_FAILURE;
    }

    char line[8192];

    // read every line from the input file
    while (fgets(line, sizeof(line), input) != NULL) {
        // find first new line or return and assign it a null string terminator
        line[strcspn(line, "\r\n")] = '\0';

        if (line[0] == '\0') {
            continue;
        }

        // get first tab separator
        // bc the data is written as:
        // IDENTIFIER /tab/ fps
        char *separator = strchr(line, '\t');

        if (separator == NULL) {
            fprintf(stderr, "Invalid input record: %s\n", line);
            fclose(input);
            free_tree(root);
            return EXIT_FAILURE;
        }

        // assign this separator a null string terminator
        // so we can separate the type and the lexeme
        *separator = '\0';

        // type points to the beginning of the line
        const char *type = line;

        // lexeme points to the character after tab
        const char *lexeme = separator + 1;

        root = insert(root, type, lexeme);
    }

    fclose(input);

    FILE *output = fopen(output_name, "w");

    if (output == NULL) {
        perror("Could not open symbol table output file");
        free_tree(root);
        return EXIT_FAILURE;
    }

    fprintf(output, "Position\tType\tLexeme\n");
    print_in_order(root, output);

    fclose(output);
    free_tree(root);

    return EXIT_SUCCESS;
}
