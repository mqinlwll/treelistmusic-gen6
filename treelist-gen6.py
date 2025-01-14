import os

def generate_tree_html(path):
    """
    Recursively generates HTML for a file and folder tree.
    """
    tree_html = '<ul>'
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            tree_html += f'<li><span class="folder">{item}</span>'
            tree_html += generate_tree_html(item_path)
            tree_html += '</li>'
        else:
            tree_html += f'<li><span class="file">{item}</span></li>'
    tree_html += '</ul>'
    return tree_html

def generate_html(folder_path):
    """
    Reads the template, generates the tree HTML, and writes the output HTML file.
    """
    with open("template.html", "r") as template_file:
        html_template = template_file.read()

    tree_html = generate_tree_html(folder_path)

    # Write the final HTML output
    with open("treelist.html", "w") as output_file:
        output_file.write(html_template.format(tree_structure=tree_html))

if __name__ == "__main__":
    folder_path = input("Enter the folder path to generate tree view: ").strip()
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        generate_html(folder_path)
        print("Tree view generated successfully in 'treelist.html'.")
    else:
        print("Invalid folder path. Please try again.")
