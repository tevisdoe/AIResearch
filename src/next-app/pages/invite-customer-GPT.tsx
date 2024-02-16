import React, { useState } from 'react';
import type { NextPage, GetServerSideProps } from 'next';
import { useRouter } from 'next/router';
import axios from 'axios';
import apiUrl from '../constants/api-url';
import Cookies from 'js-cookie';
import * as cookie from 'cookie';



const InvitePage: NextPage = (props: any) => {
  const [email, setEmail] = useState<string>('');
  const router = useRouter();
  const access_token = Cookies.get('access');

  const handleEmailChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value);
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    const valuesToSend = {
      email: email,
      is_expired: false,
      is_used: false,
      customer: props.customer.id,
    }

    try {
      const res = await axios.post(`${apiUrl}/shops/simple-invitations/`, valuesToSend, {
        headers: { Authorization: `JWT ${access_token}` },
      });
      if (res.status === 201) {
        router.push('/invite-list-co-pilot');
        return true;
      }
    } catch (error: any) {
      console.error(error);
      return false;
    }
    
  };

  // Custom back logic
  const handleBack = () => {
    router.push('/invite-list-co-pilot');
  };

  return (
    <div style={{ textAlign: 'center', fontFamily: 'Helvetica Neue', height: '100vh', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
      {/* Back button with enlarged left arrow */}
      <button
        onClick={handleBack}
        style={{ position: 'absolute', left: '10px', top: '10px', fontSize: '30px', background: 'none', border: 'none' }}
      >
        &#8592;
      </button>

      {/* Title */}
      <h1 style={{ fontSize: '30px' }}>Invite Customers</h1>

      {/* Invite form with styling */}
      <form
        onSubmit={handleSubmit}
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          maxWidth: '800px',  // Increased maximum width for better readability
          margin: 'auto',
          textAlign: 'left',
        }}
      >
        <label style={{ display: 'block', marginBottom: '20px', width: '100%', fontSize: '24px' }}>
          Email:
          <input
            type="email"
            value={email}
            onChange={handleEmailChange}
            required
            style={{ width: '100%', padding: '15px', boxSizing: 'border-box', fontSize: '20px' }}
          />
        </label>
        <button
          type="submit"
          style={{
            backgroundColor: 'green',
            color: 'white',
            padding: '20px',
            border: 'none',
            borderRadius: '10px',
            cursor: 'pointer',
            width: '100%',
            fontSize: '24px',
          }}
        >
          Invite
        </button>
      </form>
    </div>
  );
};

export const getServerSideProps: GetServerSideProps<{}> = async (context) => {
  const parsedCookies = cookie.parse(String(context.req.headers.cookie));
  const access_token = parsedCookies.access;

  try {
    const customer = await axios.get(`${apiUrl}/auth/users/me`, {
      headers: { Authorization: `JWT ${access_token}` },
    });
    return {
      props: {
        customer: customer.data,
      },
    };
  } catch (error) {
    console.log(error);
    return {
      notFound: true,
    };
  }
};

export default InvitePage;
