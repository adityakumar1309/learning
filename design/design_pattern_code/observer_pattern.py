#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://code.activestate.com/recipes/131499-observer-pattern/

*TL;DR80
Maintains a list of dependents and notifies them of any state changes.

Examples :

1) Splitwise group : Anyone adds or updates any entry in the group - all members of group get a notification .

2) Facebook : If one follows a post , he gets added to the observers & any further comments on the same post , send a notification to all the other observers ; same as twitter or any other social media follow use case .

3) Software Repository : Under the push notification model , devices are observable for the central software repository & as soon as there is new software from one of the observers , all the devices registered will be sent a push notification to check for that software.

4) When you subscribe to any website.

You are on observer in this case who has subscribed to a website (Subject) for getting notified about its post.

5) Follow feature on Quora.

As I can see right now, there are 18 followers of this question. As soon as I click on Submit after writing my answer, Quora (Subject) will send a notification to all 18 followers (observers).

6) Cricket Display

The scoreboard display, displays the average score etc information as per the current status of the match. Whenever any score changes, the scoreboard gets refreshed. So, display board is the observer here and Subject is the panel sending the current score status to the board.

7) The newspaper boy who comes at your home. Refer to this post to understand this example.

8) Whatsapp Group

Whenever any person sends any message in the group, all the people who are in the group get notified.
"""

from __future__ import print_function


class Subject(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


# Example usage
class Data(Subject):

    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class HexViewer:

    def update(self, subject):
        print(u'HexViewer: Subject %s has data 0x%x' %
              (subject.name, subject.data))


class DecimalViewer:

    def update(self, subject):
        print(u'DecimalViewer: Subject %s has data %d' %
              (subject.name, subject.data))


# Example usage...
def main():
    data1 = Data('Data 1')
    data2 = Data('Data 2')
    view1 = DecimalViewer()
    view2 = HexViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view2)
    data2.attach(view1)

    print(u"Setting Data 1 = 10")
    data1.data = 10
    print(u"Setting Data 2 = 15")
    data2.data = 15
    print(u"Setting Data 1 = 3")
    data1.data = 3
    print(u"Setting Data 2 = 5")
    data2.data = 5
    print(u"Detach HexViewer from data1 and data2.")
    data1.detach(view2)
    data2.detach(view2)
    print(u"Setting Data 1 = 10")
    data1.data = 10
    print(u"Setting Data 2 = 15")
    data2.data = 15


if __name__ == '__main__':
    main()

### OUTPUT ###
# Setting Data 1 = 10
# DecimalViewer: Subject Data 1 has data 10
# HexViewer: Subject Data 1 has data 0xa
# Setting Data 2 = 15
# HexViewer: Subject Data 2 has data 0xf
# DecimalViewer: Subject Data 2 has data 15
# Setting Data 1 = 3
# DecimalViewer: Subject Data 1 has data 3
# HexViewer: Subject Data 1 has data 0x3
# Setting Data 2 = 5
# HexViewer: Subject Data 2 has data 0x5
# DecimalViewer: Subject Data 2 has data 5
# Detach HexViewer from data1 and data2.
# Setting Data 1 = 10
# DecimalViewer: Subject Data 1 has data 10
# Setting Data 2 = 15
# DecimalViewer: Subject Data 2 has data 15
