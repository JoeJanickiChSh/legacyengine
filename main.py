import render
import window
import event


def main():
    WINDOW_SIZE = (800, 600)
    window.init(WINDOW_SIZE)
    render.init(WINDOW_SIZE)
    events = event.Events()
    while True:
        event.get_events(events)
        render.render()


if __name__ == '__main__':
    main()
