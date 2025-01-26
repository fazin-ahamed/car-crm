import unittest
from unittest.mock import patch
from backend.jobs import schedule_job, execute_job

class TestBackgroundJobs(unittest.TestCase):

    @patch('backend.jobs.schedule_job')
    def test_schedule_job(self, mock_schedule_job):
        # Test scheduling a job
        job_id = schedule_job('test_job', '2023-01-01 00:00:00')
        mock_schedule_job.assert_called_once_with('test_job', '2023-01-01 00:00:00')
        self.assertIsNotNone(job_id)

    @patch('backend.jobs.execute_job')
    def test_execute_job(self, mock_execute_job):
        # Test executing a job
        result = execute_job('test_job')
        mock_execute_job.assert_called_once_with('test_job')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
