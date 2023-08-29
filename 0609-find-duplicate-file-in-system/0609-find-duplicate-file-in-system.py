
class Solution:
    def findDuplicate(self, paths):
        content_to_paths = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]
            for file_info in parts[1:]:
                file_parts = file_info.split('(')
                file_name = file_parts[0]
                content = file_parts[1][:-1]  # Remove the closing parenthesis ')'
                full_path = f"{directory}/{file_name}"
                content_to_paths[content].append(full_path)

        duplicate_groups = [group for group in content_to_paths.values() if len(group) > 1]

        return duplicate_groups
