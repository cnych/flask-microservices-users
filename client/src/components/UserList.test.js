import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';
import UserList from './UserList';

const users = [
    {
        'active': true,
        'email': 'icnych@gmail.com',
        'id': 1,
        'username': 'cnych'
    }, {
        'active': true,
        'email': 'qikqiak@gmail.com',
        'id': 2,
        'username': 'qikqiak'
    }
];

test('UserList renders properly', () => {
    const wrapper = shallow(<UserList users={users} />);
    const element = wrapper.find('h4');
    expect(element.length).toBe(2);
    expect(element.get(0).props.className).toBe('well');
    expect(element.get(0).props.children).toBe('icnych@gmail.com');
});

test('UserList renders a snapshot properly', () => {
    const tree = renderer.create(<UserList users={users} />).toJSON();
    expect(tree).toMatchSnapshot();
});
