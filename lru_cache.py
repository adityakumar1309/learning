class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.root = None

class LRUCache(object):
    def __init__(self, maxsize=5):
        self.cache_list = DoubleLinkedList()
        self.cache_table = {}
        self.maxsize = maxsize

    def is_full(self):
        if self.get_size() >= self.maxsize:
            return True
        return False

    def get_size(self):
        size = 0
        if self.cache_list.root is None:
            return size
        else:
            size = 1
            size = 1
            item = self.cache_list.root.next
            while item != self.cache_list.root:
                size = size + 1
                item = item.next
            return size

    def save_page(self, key):
        if self.cache_table.get(key, None) != None:
            # already in cache
            desired_node = self.cache_table[key]
        else:
            # not in cache
            desired_node = Node(key)
            self.cache_table[key] = desired_node
            if self.is_full():
                self.delete_oldest()
        self.mark_most_recent(desired_node)
        return desired_node.value

    def delete_oldest(self):
        oldest = self.cache_list.root.previous
        oldest.previous.next = self.cache_list.root
        self.cache_list.root.previous = oldest.previous
        oldest = None
        
    def mark_most_recent(self, recent_node):
        if self.cache_list.root == None:
            # list is empty
            recent_node.previous = recent_node.next = recent_node
            self.cache_list.root = recent_node
        elif recent_node.next != None and recent_node.previous != None:
            # node is already in list somewhere
            self.remove_from_middle(recent_node)
            self.add_to_head(recent_node)
        else:
            # node not in list
            self.add_to_head(recent_node)

    def add_to_head(self, new_root):
        old_root = self.cache_list.root
        tail = old_root.previous
        tail.next = new_root
        new_root.previous = tail
        old_root.previous = new_root
        new_root.next = old_root
        self.cache_list.root = new_root

    def remove_from_middle(self, new_root):
        new_root.next.previous = new_root.previous
        new_root.previous.next = new_root.next

    def get_cached_results(self):
        l = []
        item = self.cache_list.root
        if item == None:
            return []
        while item.next != self.cache_list.root:
            l.append(item.value)
            item = item.next
        l.append(item.value)
        return l

if __name__ == "__main__":
    pages = [2, 6, 2, 1, 6, 4]
    print "Pages: %s"%pages
    cache_obj = LRUCache(maxsize=3)
    print cache_obj.get_cached_results()
    for page in pages:
        prev = cache_obj.get_cached_results()
        cache_obj.save_page(page)
        print "curr: %s, add %s, new: %s"%(prev, page, cache_obj.get_cached_results())
