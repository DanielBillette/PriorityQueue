TEST_FUNCTION_STRING = "print 'Executing function at index {} (priority {})'"
TEST_COMMAND_LIST = [
    {"priority": 1,
     "function": TEST_FUNCTION_STRING.format(0, 1)},
    {"priority": 1,
     "function": TEST_FUNCTION_STRING.format(1, 1)},
    {"priority": 10,
     "function": TEST_FUNCTION_STRING.format(2, 10)},
    {"priority": 7,
     "function": TEST_FUNCTION_STRING.format(3, 7)},
    {"priority": 5,
     "function": TEST_FUNCTION_STRING.format(4, 5)},
    {"priority": 10,
     "function": TEST_FUNCTION_STRING.format(5, 10)},

    {"function": TEST_FUNCTION_STRING.format(6, "N/A")},
    {"priority": 3}
]


class PriorityQueue(object):
    def __init__(self, command_list):
        super(PriorityQueue, self).__init__()
        self.command_list = self.clean_commands(command_list)

    def execute_queue_commands(self):
        for queue_item in sorted(self.command_list, key=lambda x: x["priority"]):
            # Would prefer to use partials
            # queue_item["function"]()
            exec queue_item["function"]

    @staticmethod
    def clean_commands(command_list):
        if not isinstance(command_list, list):
            return [{"priority": 1, "function": "print 'Improper command list format'"}]
        for queue_item in command_list:
            if not isinstance(queue_item, dict):
                continue

            if not queue_item.get("priority"):
                queue_item["priority"] = 10
            if not queue_item.get("function"):
                queue_item["function"] = "print 'I forgot to set a command! " \
                                         "(priority {})'".format(queue_item["priority"])

        return command_list


if __name__ == '__main__':
    priority_queue = PriorityQueue(TEST_COMMAND_LIST)
    priority_queue.execute_queue_commands()
