import event
import obj
import render
import window


def main():
    WINDOW_SIZE = (800, 600)
    window.init(WINDOW_SIZE, "Game")
    render.init(WINDOW_SIZE)
    events = event.Events()

    test_scene = obj.parse('assets/models/test_scene.obj')
    scene = [test_scene]

    while True:
        event.get_events(events)
        render.render(scene)


if __name__ == '__main__':
    main()
