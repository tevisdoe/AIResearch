import type { NextPage, GetServerSideProps } from 'next';
import axios from 'axios';
import Header from '../components/Header';
import 'moment-timezone';
import apiUrl from '../constants/api-url';
// @ts-ignore
import * as cookie from 'cookie';
import { Radio } from '@mantine/core';
import { useState } from 'react';
import Cookies from 'js-cookie';
import { useRouter } from 'next/router';
import { BsPlus } from 'react-icons/bs';

const InviteListCoPilot: NextPage = ({ customerInvitations }: any) => {
  const router = useRouter();
  const [errors, setErrors] = useState([]);
  const [sortStatus, setSortStatus] = useState('all');
  const invitationList = customerInvitations
    .filter((customerInvitation: any) => {
      if (sortStatus === 'not_expired') {
        return !customerInvitation.is_expired;
      } else if (sortStatus === 'not_used') {
        return !customerInvitation.is_used;
      }
      return true;
    })
    .map((customerInvitation: any) => {
      return (
        <div key={customerInvitation.invitation_key} className="card">
          <div className="flex flex-col row-gap-small">
            <span>
              <b>Email</b>: {customerInvitation.email}
            </span>
            <span>
              <b>Expiry</b>: {customerInvitation.is_expired ? 'Expired' : 'Not Expired'}
            </span>
            <span>
              <b>Used</b>: {customerInvitation.is_used ? 'Used' : 'Not Used'}
            </span>
            <span>
              <b>Invitation Key</b>: {customerInvitation.invitation_key}
            </span>
            <span>
              <b>Customer ID</b>: {customerInvitation.customer}
            </span>
            <button
              className="delete-button cursor-pointer hover-scale-up active-scale-down"
              onClick={() => deleteInvitation(customerInvitation.invitation_key)}
            >
              Delete
            </button>
          </div>
        </div>
      );
    });

  const deleteInvitation = async (invitation_key: string) => {
    const access_token = Cookies.get('access');
    try {
      const res = await axios.delete(`${apiUrl}/shops/simple-invitations/${invitation_key}/`, {
        headers: { Authorization: `JWT ${access_token}` },
      });
      if (res.status === 204) {
        router.reload();
      }
    } catch (error: any) {
      setErrors(error.response.data?.errors);
      scrollTo(0, 0);
    }
  };
  return (
    <div className="container">
      <Header
        title="Friend Invitations"
        backButtonPath="/dashboard"
        rightIcon={BsPlus}
        onRightIconClick={() => router.push('/invite-customer-GPT')}
      />
      <div className="wrapper">
        {errors?.length > 0 && (
          <div className="flex flex-col row-gap-small">
            {errors.map((error: any, index) => {
              return (
                <span className="error" key={`error_${index}`}>
                  {error.detail}
                </span>
              );
            })}
          </div>
        )}
        <div className="flex flex-col">
          <Radio.Group
            label="Filter by Status"
            defaultValue={sortStatus}
            style={{ paddingBottom: '10px' }}
            onChange={(value) => setSortStatus(value)}
          >
            <Radio value="all" label="All" />
            <Radio value="not_expired" label="Not Expired" />
            <Radio value="not_used" label="Not Used" />
          </Radio.Group>
        </div>
        <div className="grid-list">
          {invitationList.length > 0 ? invitationList : <p>No invitations found.</p>}
        </div>
      </div>
    </div>
  );
};

export const getServerSideProps: GetServerSideProps<{}> = async (context) => {
  const parsedCookies = cookie.parse(String(context.req.headers.cookie));
  const access_token = parsedCookies.access;
  try {
    const customerInvitations = await axios.get(`${apiUrl}/shops/simple-invitations/`, {
      headers: { Authorization: `JWT ${access_token}` },
    });
    const customer = await axios.get(`${apiUrl}/auth/users/me`, {
      headers: { Authorization: `JWT ${access_token}` },
    });
    // I really shouldn't be filtering the invitations in the front end, but I'm doing it just for the proof of concept.
    const customerInvitesFiltered = customerInvitations.data.filter((customerInvitation: any) => {
      return customerInvitation.customer === customer.data.id;
    });

    return {
      props: {
        customerInvitations: customerInvitesFiltered,
      },
    };
  } catch (error) {
    console.log(error);
    return {
      notFound: true,
    };
  }
};

export default InviteListCoPilot;
