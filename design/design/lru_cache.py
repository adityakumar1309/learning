class Node:
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.nxt = nxt

class DoubleLinkedList:
    def __init__(self):
        self.root = None

class LRUCache:
    def __init__(self, maxsize):
        self.cache_list = DoubleLinkedList()
        self.cache_table = {}
        self.maxsize = maxsize

    def save_page(self, key):
        if key in self.cache_table:
            # already in cache
            desired_node = self.cache_table[key]
        else:
            # not in cache
            desired_node = Node(key)
            if len(self.cache_table) >= self.maxsize:
                #if cache is full
                self.delete_oldest()
            self.cache_table[key] = desired_node
        self.mark_most_recent(desired_node)

    def delete_oldest(self):
        oldest = self.cache_list.root.prev
        self.cache_table.pop(oldest.value)
        oldest.prev.nxt = self.cache_list.root
        self.cache_list.root.prev = oldest.prev
        oldest = None
        
    def mark_most_recent(self, recent_node):
        if self.cache_list.root == None:
            # list is empty
            recent_node.nxt = recent_node
            recent_node.prev = recent_node
            self.cache_list.root = recent_node
        elif recent_node == self.cache_list.root:
            #if recent node is already the most recent then do nothing
            return
        elif recent_node.nxt != None and recent_node.prev != None:
            # node is already in list somewhere
            self.remove_from_middle(recent_node)
            self.add_to_head(recent_node)
        else:
            # node not in list
            self.add_to_head(recent_node)

    def add_to_head(self, new_root):
        old_root = self.cache_list.root
        tail = old_root.prev
        tail.nxt = new_root
        new_root.prev = tail
        old_root.prev = new_root
        new_root.nxt = old_root
        self.cache_list.root = new_root

    def remove_from_middle(self, new_root):
        new_root.nxt.prev = new_root.prev
        new_root.prev.nxt = new_root.nxt

    def get_cached_results(self):
        l = []
        item = self.cache_list.root
        if item == None:
            return []
        while item.nxt != self.cache_list.root:
            l.append(item.value)
            item = item.nxt
        l.append(item.value)
        return l

if __name__ == "__main__":
    pages = [2, 6, 2, 1, 6, 4, 4, 3]
    print "Pages: %s"%pages
    maxsize = 3
    cache_obj = LRUCache(maxsize)
    print cache_obj.get_cached_results()
    for page in pages:
        #print "Len of hash map: %s"%(len(cache_obj.cache_table))
        prev = cache_obj.get_cached_results()
        cache_obj.save_page(page)
        print "curr: %s, add %s, new: %s"%(prev, page, cache_obj.get_cached_results())
