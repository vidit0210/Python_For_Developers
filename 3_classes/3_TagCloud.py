class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.tags.get(tag, 0)

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add('python')
cloud.add('Python')
cloud.add('Python')
cloud.add('javaScript')
print(len(cloud))  # Gives number of keys
