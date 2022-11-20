


class Functions:
    def switch_to_learn(self, switch, location, placeholder, is_valid, flashcard_function_call):
        if is_valid:
            if location == 'learn':
                return switch.setCurrentIndex(switch.currentIndex() + 1)
            elif location == 'flashcard':
                return switch.setCurrentIndex(switch.currentIndex() + 2)

        else:
            self.error_prompt(placeholder)

    def return_home(self, switch):
        return switch.setCurrentIndex(0)


    def error_prompt(self, holder):
        holder.setText('')
        holder.setPlaceholderText('Please paste a Valid Quizlet link')
