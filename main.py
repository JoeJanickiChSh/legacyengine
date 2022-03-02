from cgi import test
import render
import window
import event
import obj


def main():
    WINDOW_SIZE = (800, 600)
    window.init(WINDOW_SIZE, "Game")
    render.init(WINDOW_SIZE)
    events = event.Events()

    test_scene = obj.parse('assets/models/test_scene.obj')

    for v in test_scene:
        print(v)

    while True:
        event.get_events(events)
        render.render()


if __name__ == '__main__':
    main()
