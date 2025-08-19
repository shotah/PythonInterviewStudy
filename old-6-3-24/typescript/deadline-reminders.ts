interface Task {
  task: string;
  dueDate: string;
}

export function printReminders(tasks: Task[]): void {
  const today = new Date();

  tasks.forEach(({ task, dueDate }) => {
    const due = new Date(dueDate);
    const daysRemaining = Math.ceil((due.getTime() - today.getTime()) / (1000 * 60 * 60 * 24));

    if (daysRemaining < 0) {
      console.log(`OVERDUE: ${task} was due ${-daysRemaining} day(s) ago`);
    } else {
      console.log(`${task} is due in ${daysRemaining} day(s)`);
    }
  });
}
