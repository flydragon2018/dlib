import xml.etree.ElementTree as etree


def remove_tag(root, tag_id_r):
    tags_elem = root.find("tags")
    target_tag = tags_elem.find(f"tag[@id='{tag_id_r}']")
    if target_tag:
        tags_elem.remove(target_tag)
    else:
        print(f"A tag with the id \"{tag_id_r}\" cannot be found.")


def main():
    tree = etree.parse("remove_demo.xml")
    root = tree.getroot()

    remove_tag(root, input("What is the id of the tag you want to remove? "))

    # Overwriting the input file. Are you sure that's a good idea?
    tree.write("removed_demo.xml", encoding="utf-8")


main()